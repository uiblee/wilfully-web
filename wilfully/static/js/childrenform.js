$(document).ready(function(){

  $('#children').on('change', function onChildrenChange(){
    if (this.checked) {
      $('.child-dependant').show();
    } else {
      $('.child-dependant').hide();
    }
  });

  var childWidget = function(index){
    //clone the first child.
    var template = $('.children .form-group:eq(0)').clone();
    var $label = template.find('label');
    var $input = template.find('input');
    // clear the input.
    $input.val('');
    // fix the attributes
    $label.attr('for', 'childrenname-'+index);
    $input.attr('name', 'childrenname-'+index);
    $input.attr('id', 'childrenname-'+index);
    return template;
  };

  $('#childrennumber').on('change', function onChildrenNumberChange(){
    if (isNaN(this.valueAsNumber)) { alert("Don't do that please, put just a number!"); }
    else {
      var childrenNumber = this.valueAsNumber;
      var widgetNumber = $('.children .form-group').length;

      // Add more widgets
      if (childrenNumber > widgetNumber) {
        var difference = childrenNumber - widgetNumber;
        for (var index = 1; index <= difference; index++) {
          $('.children').append(childWidget(widgetNumber+index-1));
        }
      }
      // Remove widgets
      else if (childrenNumber < widgetNumber) {
        var difference = widgetNumber - childrenNumber;
        for (var index = widgetNumber; index >= difference; index--) {
          $('.children').remove(childWidget(widgetNumber));
        }
      }

    }
  });

});


//(function($, window) {}).call(this, jQuery, window);
