var acc = window.document.querySelector(".news_tab");
var news_wrapper = acc.nextElementSibling;

acc.addEventListener("click touchstart", function() {
    /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
    acc.classList.toggle("active");
    
//    document.getElemen
    
        /* Toggle between hiding and showing the active panel */
//    if (news_wrapper.style.display === "block") {
//        news_wrapper.style.display = "none";
//    } else {
//        news_wrapper.style.display = "block";
//    }
//    
    
    if (news_wrapper.style.maxHeight) {
      news_wrapper.style.maxHeight = null;
      acc.innerHTML = "펼치기";
    } else {
      acc.innerHTML = "접기";
      news_wrapper.style.maxHeight = news_wrapper.scrollHeight + "px";
    }
});