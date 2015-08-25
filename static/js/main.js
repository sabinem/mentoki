/**
 * Created by sabinemaennel on 06.08.15.
 */

$(document).ready(function(){

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


/**
 * from http://davidwalsh.name/mootools-drag-ajax
 * for sorting formsets
 */

/* when the DOM is ready */
window.addEvent('domready', function() {
	/* grab important elements */
	var sortInput = document.id('sort_order');
	var submit = document.id('autoSubmit');
	var messageBox = document.id('message-box');
	var list = document.id('sortable-list');

	/* get the request object ready;  re-use the same Request */
	var request = new Request({
		url: '<?php echo $_SERVER["REQUEST_URI"]; ?>',
		link: 'cancel',
		method: 'post',
		onRequest: function() {
			messageBox.set('text','Updating the sort order in the database.');
		},
		onSuccess: function() {
			messageBox.set('text','Database has been updated.');
		}
	});
	/* worker function */
	var fnSubmit = function(save) {
		var sortOrder = [];
		list.getElements('li').each(function(li) {
			sortOrder.push(li.retrieve('id'));
		});
		sortInput.value = sortOrder.join(',');
		if(save) {
			request.send('sort_order=' + sortInput.value + '&ajax=' + submit.checked + '&do_submit=1&byajax=1');
		}
	};

	/* store values */
	list.getElements('li').each(function(li) {
		li.store('id',li.get('title')).set('title','');
	});

	/* sortables that also *may* */
	new Sortables(list,{
		constrain: true,
		clone: true,
		revert: true,
		onComplete: function(el,clone) {
			fnSubmit(submit.checked);
		}
	});

	/* ajax form submission */
	document.id('dd-form').addEvent('submit',function(e) {
		if(e) e.stop();
		fnSubmit(true);
	});


});
