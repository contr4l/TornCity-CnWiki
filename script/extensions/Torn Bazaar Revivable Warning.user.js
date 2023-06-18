// ==UserScript==
// @name         Torn Bazaar Revivable Warning
// @namespace    http://contr4l.github.io/
// @version      1.0
// @description  try to take over the world!
// @author       contr4l_ [2893026]
// @match        https://www.torn.com/bazaar.php
// @icon         https://www.google.com/s2/favicons?sz=64&domain=torn.com
// @grant        none
// ==/UserScript==

async function fetchContent(url) {
    const res = await fetch(url);
    const text = await res.text();
    const parser = new DOMParser();
    const htmlDoc = parser.parseFromString(text, 'text/html');

    return new Promise(resolve => {
        requestIdleCallback(() => {
            resolve(htmlDoc);
        });
    });
}
  

function detect_revivable() {
    var revivable = ""
    let hos_url = "https://www.torn.com/hospitalview.php";
    let res = fetchContent(hos_url);
    res.then(doc => {
        revivable = doc.getElementById("revive-availability").textContent;
        console.log(revivable);
        if (revivable != "Nobody") {
            alert("请注意，你没有关闭复活!");
        }
    });
}

(function() {
    'use strict';
    setTimeout(detect_revivable(), 1000);
    // Your code here...
})();