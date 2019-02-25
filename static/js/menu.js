window.onload = function () {
    var flag = true;
    var liC = document.querySelectorAll(".navBox li h2");

    // 隐藏菜单
    var obscure = document.querySelector(".navH span");
    var open = document.querySelector("#open");
    var ensconce = document.querySelector("#ensconce");
    obscure.onclick = function () {
        open.style.marginLeft = "-300px";
        setTimeout(function () {
            ensconce.style.display = "block";
        }, 350)

    }
    //显示菜单
    var showC = document.querySelector("#ensconce h2");
    showC.onclick = function () {
        open.style.marginLeft = "0px";
        setTimeout(function () {
            ensconce.style.display = "none";
        }, 100)

    }
}

function getByClass(clsName, parent) {
    var oParent = parent ? document.getElementById(parent) : document,
        boxArr = new Array(),
        oElements = oParent.getElementsByTagName('*');
    for (var i = 0; i < oElements.length; i++) {
        if (oElements[i].className == clsName) {
            boxArr.push(oElements[i]);
        }
    }
    return boxArr;
}
