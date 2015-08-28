/**
 * Created by sabinemaennel on 06.08.15.
 */

$(document).ready(function(){

    $(function() {
        $('#edit').editable({key: 'tckD-17B1ewrwA-7sekA2ys=='});
    });

/**
 * correct ui classes for user input through editor
 */
    // add ui class
    $("#mentoki table").addClass("ui celled compact table");
    $("#mentoki img").addClass("ui img");
    $("#mentoki ul").addClass("ui list");
    $("#mentoki ol").addClass("ui list");

// accordion
    $('.ui.accordion')
       .accordion()
    ;

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

  function checkForm(form) // Submit button clicked
  {
    //
    // check form input values
    //
    form.onlyOnceButton.disabled = true;
    form.onlyOnceButton.value = "Bitte warten ...";
    return true;
  }

  function resetForm(form) // Reset button clicked
  {
    form.onlyOnceButton.disabled = false;
    form.onlyOnceButton.value = "Speichern";
  }

  $('#formsubmit_button').on('click', function(){
      this.disabled=true,
      this.form.submit()
    });


});


