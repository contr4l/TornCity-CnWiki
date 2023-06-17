// ==UserScript==
// @name         Yata Price Enhancer
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  show difference rate comparing to TT price
// @author       contr4l_ [2893026]
// @match        https://yata.yt/bazaar/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

function num_trans(price)
{
    return Number(price.replace("$", "").replaceAll(",", ""))
}

function cal_rate(cur_price, TT_price)
{
    let rate = (cur_price - TT_price) / TT_price;
    return (100*rate).toFixed(2) + "%";
}

function get_TT_price(child_row)
{
    let TT_price = child_row[4].querySelector('div').querySelector("a").textContent;
    TT_price = num_trans(TT_price);
    return TT_price;
}

function add_rate_info(tr, TT_price)
{
    // console.log(tr);

    let tds = tr.querySelectorAll('td');
    if (tds.length < 2){
        return; // Show more...
    }

    let price = tds[1].textContent;

    if (price == 0){
        return;
    }
    // console.log("price is " + price);
    price = num_trans(price);
    // console.log("price is " + price + " TT_price is " + TT_price);
    let rate_text = cal_rate(price, TT_price);
    tds[0].setAttribute('style', 'width: 10%;');
    tds[1].setAttribute('style', 'width: 60%;');
    let cell = tr.insertCell();
    cell.innerText = rate_text;
}


(function() {
    'use strict';
    console.log("Yata Enhancer Start!");
    var items_table = document.querySelectorAll('.col.item-table.p-0.mx-1.mb-2');
    items_table.forEach(element => {
        //console.log("Find item, item's id is ");
        //console.log(element.getAttribute("data-iid"));
        var child_row = element.querySelectorAll('.col-12.px-4');

        let name = child_row[2].getAttribute("title");
        // console.log("item name is " + name);

        let TT_price = get_TT_price(child_row);
        // console.log("price is " + TT_price);

        let table_ = element.querySelector('tbody');

        let trs_ = table_.querySelectorAll("tr");
        trs_.forEach( tr_ => {
            add_rate_info(tr_, TT_price);
        });
    });
})();