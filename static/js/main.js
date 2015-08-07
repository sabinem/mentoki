/**
 * Created by sabinemaennel on 06.08.15.
 */

$(document).ready(function(){

    selector    : {
      popup    : '.ui.popup'
    }


    // add ui class
    $("#ui_textdisplay table").addClass("ui celled compact table");
    $("#ui_textdisplay img").addClass("ui img");
    $("#ui_textdisplay ul").addClass("ui list");
    $("#ui_textdisplay ol").addClass("ui list");

    //$(function () {
    //    $('a.item').click(function(){
    //       $('.item').removeClass('active');
    //       $(this).addClass('active');
    //   })
    //});

    // Button for sidebar
    $('#sidebar_button').on('click', function(){
       $('#coursemenu').sidebar('toggle', 'overlay');
    });

    // showing multiple
    $('.context.example .ui.sidebar')
      .sidebar({
        context: $('.context.example .bottom.segment')
      })
      .sidebar('attach events', '.context.example .menu .item')
    ;

    $('.menu .browse')
      .popup({
        inline   : true,
        hoverable: true,
        position : 'bottom left',
        delay: {
          show: 300,
          hide: 800
        }
      })
    ;

    $('.button.worklinks')
      .popup({
        inline   : true,
        hoverable: true,
        position : 'bottom left',
        delay: {
          show: 300,
          hide: 800
        }
      })
    ;

    $('.worklinks')
      .popup({
        inline   : true,
        hoverable: true,
        position : 'bottom left',
        delay: {
          show: 300,
          hide: 800
        }
      })
    ;

});
