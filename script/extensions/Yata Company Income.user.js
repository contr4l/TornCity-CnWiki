// ==UserScript==
// @name         Yata Company Income
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Download all company records in Yata
// @author       contr4l_[2893026]
// @match        https://yata.yt/company/supervise/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=yata.yt
// @grant        none
// ==/UserScript==

function deleteBracket(content) {
    let regex = / *\([^)]*\) */g;
    const newStr = content.replace(regex, "");

    regex = /[,$\ ]/g;

    return newStr.replace(regex, "");
}

function appendTableData(table, ignore_header = 0) {
    const rows = table.rows;
    let res = "";

    console.log(rows);

    for (let i = 0; i < rows.length - 1; i++) {
        let rowData = []
        if (ignore_header == 1 && i == 0)
        {
            continue;
        }

        for (let j = 0; j < rows[i].cells.length; j++) {

            rowData.push(deleteBracket(rows[i].cells[j].innerText));
        }
        if (rowData) {
            res += rowData.join(",") + "\n"
        }
    }
    return res;
}

function downloadTable(csvContent) {
    const encodedUri = encodeURI(csvContent)
    const link = document.createElement("a")
    link.setAttribute("href", encodedUri)
    link.setAttribute("download", "Company_Record.csv")
    document.body.appendChild(link)
    link.click()
}

async function captureData() {
    let element = document.querySelector(".yt-page-link.rounded.last");
    let url = element["href"];
    let baseurl = url.split("=")[0];
    let lastPageId = Number(url.split("=")[1]);
    var csvContent = "data:text/csv;charset=utf-8,";

    for (let i=1; i<=lastPageId; i++) {
        let request_url = baseurl + "=" + i;
        const response = await fetch(request_url);
        const html = await response.text();
        const res = new DOMParser().parseFromString(html, "text/html");
        let table_data = res.querySelector(".table");
        csvContent += appendTableData(table_data, i!=1);
    }
    console.log("res=", csvContent);
    downloadTable(csvContent);
}

function buildChildDiv(){
    const childDiv = document.createElement("div");
    childDiv.setAttribute('class', "px-2");

    const childA = document.createElement("a");
    childA.setAttribute('id', "download_record");

    const childI = document.createElement("i");
    childI.setAttribute('class', "fas fa-file-export");
    childI.setAttribute('title', "Export Company Record to CSV");

    childA.appendChild(childI);
    childA.appendChild(document.createTextNode(" Export Company Record"));

    childDiv.appendChild(childA);
    return childDiv;
}

(function() {
    'use strict';
    let div_ = document.querySelector('.row.justify-content-between');
    div_.setAttribute('class', 'd-flex flex-wrap align-items-center');
    let brother = div_.querySelector('.col');
    brother.setAttribute('class', 'px-2 me-auto');

    let child = buildChildDiv();
    div_.appendChild(child);

    document.getElementById('download_record').onclick = function() {
        captureData();
    };
})();