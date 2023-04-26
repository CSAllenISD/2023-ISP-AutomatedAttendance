function addPeriod(periodId) {
    fetch("/delete-period", {
      method: "POST",
      body: JSON.stringify({periodId: periodId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }