var modal = document.getElementById("myModal");
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];
var modalBtn = document.getElementsByClassName("modal__btn")[0];

var editModeBtn = document.getElementById("editModeBtn");
var saveBtn = document.getElementById("saveBtn");
var td = document.querySelectorAll("[id='removeButton']");
var editableText = document.getElementById("edit");

editModeBtn.onclick = function() {
  for(var i = 0; i < td.length; i++)
    td[i].style.display = "block";
  
  editModeBtn.style.display = "none";
  saveBtn.style.display = "inline-block";
}

saveBtn.onclick = function() {
  for(var i = 0; i < td.length; i++)
    td[i].style.display = "none";
  
  editModeBtn.style.display = "inline-block";
  saveBtn.style.display = "none";
}

function studentCount() {
    var table = document.getElementById("tableID").rows.length - 1;
    document.getElementById("countDisplay").innerHTML = table + " students";
}

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

modalBtn.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
}

function filterFunction() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("tableID");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }       
    }
}

