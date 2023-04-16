var selectall_button = document.getElementById('select-all');

selectall_button.addEventListener("click", () =>{
   var checkboxes = document.getElementsByName('organ');
   for(var checkbox of checkboxes){
      if(selectall_button.checked === true){
         checkbox.checked = true;
      }
      else{
         checkbox.checked = false;
      }
   }
})