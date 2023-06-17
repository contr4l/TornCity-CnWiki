// ==UserScript==
// @name         NGA CheckIn Stats
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  一键统计NGA论坛中本月发布回帖的人数。
// @author       contr4l_ [2893026]
// @match        https://nga.178.com/read.php?tid=20217469*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=178.com
// @grant        none
// ==/UserScript==

var csvContent = "data:application/vnd.ms-excel;charset=utf-8,";
csvContent += '\ufeff'; // 添加BOM头
csvContent += '"楼层","发帖时间","发帖人"\n';

var invalidContent = "data:application/vnd.ms-excel;charset=utf-8,";
invalidContent += '\ufeff'; // 添加BOM头
invalidContent += '"不合格楼层","发帖时间","不合格发帖人"\n';


function get_page_final() {
    let div = document.getElementById("m_pbtntop").querySelector(".left");
    let table = div.querySelector(".stdbtn");
    let tds = table.querySelectorAll("td");
    let td = tds[tds.length - 4];
    let final_page = td.querySelector("a").href;
    return final_page;
}

function time_in_range(t) {
    function get_month(s) {
        let ymd = String(s).split(" ")[0];
        return Number(ymd.split("-")[1]);
    }

    let now = new Date();
    return now.getMonth() <= get_month(t);
}

function validate_post(content) {
    // 带图10字；不带图50字
    // <img src="about:blank" style="display:none" onerror="ubbcode.copyChk(this.parentNode,&quot;postcontent18&quot;)">
    // <img class="smile_ac" src="https://img4.nga.178.com/ngabbs/post/smile/ac15.png" alt="哭笑">
    // <img style="max-height: none; min-height: 963px; min-width: 1175px; max-width: 1492px;" onload="ubbcode.adjImgSize(this,1288.4);" onerror="ubbcode.imgError(this)" onclick="" _orgt="0" src="https://img.nga.178.com/attachments/mon_202306/09/bwQ4lll-f802K2cT3cSwn-qr.png" data-srcorg="https://img.nga.178.com/attachments/mon_202306/09/bwQ4lll-f802K2cT3cSwn-qr.png" data-usethumb="" data-srclazy="" data-nw="1175" data-nh="963" data-apporg="" data-appthumb="" alt="">
    let min_words_length = 50;
    let img_list = content.querySelectorAll("img");
    img_list.forEach(img => {
        let src_url = img.src;
        let class_ = img.class;
        if (!class_)
            return;
        if (!src_url.includes("attachments"))
            return;
        else {
            min_words_length = 10;
        }
    });

    // split为了删去引用
    let text_list = content.textContent.split("\n");
    let content_length = text_list[text_list.length - 1].length;
    return content_length >= min_words_length;
}

function validate_post_json(content, subject) {
    const regex = /\[img\](.*?)\[\/img\]/g;
    let min_words_length = 50;

    while ((match = regex.exec(content)) !== null) {
        const src = match[1];
        if (src.includes("attachment")) {
            min_words_length = 10;
            break;
        }
    }

    let text_content = content.replace(regex, "");
    return text_content.length + subject.length >= min_words_length;
}

function last_elem(lst) {
    return lst[lst.length - 1];
}

function get_all_post_in_page(doc) {
    var posts = new Array();
    let post_tables = doc.querySelectorAll(".forumbox.postbox");
    post_tables.forEach(post_div => {
        let date = post_div.querySelector(".c2")
            .querySelector("span[title='reply time']")
            .textContent;

        let uid = post_div.querySelector(".c1")
            .querySelector("a")
            .href;

        let idx = post_div.querySelector(".c1")
            .querySelector("span")
            .id
            .replace("posterinfo", "");
        let content_id = "postcontent" + idx;
        let content = doc.getElementById(content_id);
        if (validate_post(content)) {
            posts.push([idx, date, uid]);
        }
    });
    return posts;
}

function get_all_post_in_json(resp) {
    var posts = new Array();
    resp["result"].forEach(post => {
        let idx = post["lou"];
        let date = post["postdate"];
        let name = post["author"]["username"];
        let content = post["content"];
        let subject = post["subject"];
        if (validate_post_json(content, subject)) {
            posts.push([idx, date, name]);
        } else {
            let log = `检测到不合格回帖，位于${idx}楼，由${name}回复`;
            invalidContent += `"${idx}","${date}","${name}"\n`
        }
    });
    return posts;
}

function processPosts(posts) {
    interrupt = false;

    for (let k = 0; k < posts.length; k++) {
        info = posts[k];
        if (time_in_range(info[1])) {
            csvContent += `"${info[0]}","${info[1]}","${info[2]}"\n`;
        }
        else {
            interrupt = true;
            break;
        }
    }
    return interrupt;
}

function processWebPage(page) {
    let posts = get_all_post_in_page(res);
    return processPosts(posts);
}

function processJsonPage(resp) {
    let posts = get_all_post_in_json(resp);
    return processPosts(posts);
}

function encodeFormData(data) {
    const pairs = [];
    for (const [key, value] of Object.entries(data)) {
        pairs.push(encodeURIComponent(key) + '=' + encodeURIComponent(value));
    }
    return pairs.join('&');
}

function sendXhrReq(data, resolve, reject) {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'app_api.php?__lib=post&__act=list');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const resp = JSON.parse(xhr.responseText);
                interrupt = processJsonPage(resp);
                resolve();
            } else {
                reject(new Error('XHR request failed'));
            }
        }
    };
    xhr.send(encodeFormData(formData));
}

async function captureData() {
    let final_page = get_page_final();
    let baseurl = "https://nga.178.com/read.php?tid=20217469&page";
    let lastPageId = Number(final_page.split("=")[2]);

    var interrupt = false;

    for (let i = lastPageId; i >= 1; i--) {
        let request_url = baseurl + "=" + i;
        const formData = {
            page: i.toString(),
            tid: "20217469"
        };

        const promise = new Promise((resolve, reject) => {
            sendXhrReq(formData, resolve, reject);
        });

        try {
            await promise;
        } catch (error) {
            console.error(error);
        }

        if (interrupt) {
            console.log("识别到非时间区间内的发帖，爬楼停止。");
            break;
        }
    }
    downloadTable();
}

function buildChildTd() {
    const childTd = document.createElement("td");

    const childA = document.createElement("a");
    childA.setAttribute('id', "nga_analyze");
    childA.appendChild(document.createTextNode("SMTH-NGA爬楼"));

    childTd.appendChild(childA);
    return childTd;
}

function downloadTable() {
    const encodedUri = encodeURI(csvContent)
    const link = document.createElement("a")
    link.setAttribute("href", encodedUri)
    link.setAttribute("download", "NGA_CheckIn_Stats.csv")
    document.body.appendChild(link)
    link.click()

    const anotherUri = encodeURI(invalidContent)
    const another_link = document.createElement("a")
    another_link.setAttribute("href", anotherUri)
    another_link.setAttribute("download", "NGA_Invalid_Reply.csv")
    document.body.appendChild(another_link)
    another_link.click()
}

(function () {
    'use strict';
    let div = document.getElementById("m_pbtntop").querySelector(".left");
    let tr = div.querySelector(".stdbtn").querySelector("tr");
    const emptyTd = document.createElement("td");
    emptyTd.setAttribute("style", "width:20px; background-color:#ffffff");
    tr.appendChild(emptyTd);

    let child = buildChildTd();
    tr.appendChild(child);

    document.getElementById('nga_analyze').onclick = function () {
        captureData();
    };
})();