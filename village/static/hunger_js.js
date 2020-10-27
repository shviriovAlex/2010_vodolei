
  $(document).ready(function(){
    $('.burger').click(function(event){
      $('.burger, .nav-box, .circle, .mobile-nav').toggleClass('active')
    });
    $('.button').click(function(btn){
      $('.button, .round-button, .button-header, .btn-header, .glad_to_see, .restaurant').toggleClass('activeBtn')
    });
    $('.menu-button').click(function(btn_menu){
      $('.menu-button, .nav-container-6, .nav-link-6').toggleClass('activeBtnMenu')
    });
    $('.btn-7').click(function (btn_7) {
      $('.btn-7, .box-1-container-7, .box-2-container-7').toggleClass('activePerformance')
    })
  
  }); 