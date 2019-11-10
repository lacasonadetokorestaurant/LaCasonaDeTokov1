/*Galeria Con Slide*/
baguetteBox.run('.gal-cont');


/*ANIMAR CARRUSEL*/
$('.carousel').carousel({
    interval: 3000,
    touch: true
});

/*Cerrar Toggle al Hacer Click en un Link*/
$(function () {
    var navMain = $(".navbar-collapse");
    navMain.on("click", "a:not([data-toggle])", null, function () {
        navMain.collapse('hide');
    });
});
/* SCROLL UP PAGINA */

window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

