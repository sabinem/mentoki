/**
 * Created by sabinemaennel on 06.08.15.
 */

$(document).ready(function(){

   // Mobile button for sidebar
   $('#mobile_button').on('click', function(){
       $('#mobile_menu').sidebar('toggle', 'overlay');
   });

/**
 * dropdown menu for public pages
 */

    $('.ui.dropdown')
      .dropdown()
    ;

/**
 * dropdown menu for public pages
 */
    $('.ui.sticky')
      .sticky({
        context: '#context'
    })
    ;


// This first part is for all pages in the Courses Section of the site
// checkboxes are special in Semantic UI
    $('.ui.checkbox')
      .checkbox()
    ;

// embed video
    $('.ui.embed')
        .embed()
    ;


// this checkbox displays the particpants form fields in preparation for
// payment, when requested
    if ($('#participant_self').checkbox('is checked')){
       $('.participant_fields').hide();
    }
    $('#participant_self').change(function(){
       if ($('#participant_self').checkbox('is checked')){
           $('.participant_fields').fadeOut();
       }
    });
    $('#participant_self').change(function(){
       if ($('#participant_self').checkbox('is unchecked')){
           $('.participant_fields').fadeIn();
       }
    });



/**
 * correct ui classes for user input through editor
 */
    // add ui class
    // $("#mentoki table").addClass("ui celled compact table");
    $("#mentoki img").addClass("ui image");
    // $("#mentoki ul").addClass("ui list");
    // $("#mentoki ol").addClass("ui list");

// accordion
    $('.ui.accordion')
       .accordion()
    ;

// embed you tube
    $('.url.example .ui.embed').embed();

/**
 * Sidebar and pusher functionality: the button opens a sidebar in Semantic UI
 * see Semantic UI/ Sidebar
 */
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


    $('.menu .courses')



/**
 * Pop up menu in the classroom and coursebackend
 * see Semantic UI/ Sidebar
 */

    selector    : {
      popup    : '.ui.popup'
    }

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

/**
 * Prevent double form submission of forms
 * copied from the internet, which source?
 */

    $('#formsubmitonce').on('click', function(){
        this.disabled=true;
        this.form.submit();
    });






});