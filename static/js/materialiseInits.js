$(document).ready(function(){
  //materialize initiations
  $('.sidenav').sidenav();
  $('.select').formSelect();
  $('.datepicker').datepicker();
  //Show/reveal on movie pages
  $('.movie-buttons').hide();
  $('.options').click(function(){
    $('.movie-buttons').toggle(1000);
  });
});