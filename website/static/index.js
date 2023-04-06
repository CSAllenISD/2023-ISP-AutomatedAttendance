function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }
  
function addPeriod(periodId) {
    fetch("/delete-period", {
      method: "POST",
      body: JSON.stringify({periodId: periodId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }
  