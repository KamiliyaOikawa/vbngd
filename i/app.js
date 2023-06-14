const tabs = document.querySelectorAll(".tabheader__item");
const tabsParent = document.querySelector(".tabheader__items");
const tabsContent = document.querySelectorAll(".slider-photo");

const hideTabContent = () => {
    tabsContent.forEach((item) => {
        item.style.display = "none";
    });
    tabs.forEach((item) => {
        item.classList.remove("tabheader__item_active");
    });
};

const showTabContent = (i = 1) => {
    tabsContent[i].style.display = "block";
    tabs[i].classList.add("tabheader__item_active");
};

hideTabContent();
showTabContent();

tabsParent.addEventListener("click", (event) => {
    const target = event.target;
    if (target.classList.contains("tabheader__item")) {
        tabs.forEach((item, i) => {
            if (target === item) {
                hideTabContent()
                showTabContent(i)
            }
        });
    }
});

let slide = 0

function slides(n) {
    if (n > tabs.length && n > tabsContent.length) {
        slide += 1;
    } else if (n < 0) {
        slide = tabs.length && slide == tabsContent.length;
    }
    for (let i of tabs) {
        i.classList.remove("tabheader__item_active")
    }
    tabs[n].classList.add("tabheader__item_active")
    for (let i of tabsContent) {
        i.style.display = "none"
    }
    tabsContent[slide].style.display = "block"
}

setInterval(() => {
    slide++;
    if (slide >= 4) {
        slide = 0
    }
    slides(slide);
}, 2000);


