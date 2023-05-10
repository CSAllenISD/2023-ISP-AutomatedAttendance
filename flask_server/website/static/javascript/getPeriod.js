function getP() {
  const now = new Date().toLocaleTimeString('en-US', {hour12: false, hour: 'numeric', minute: 'numeric'});
  const [hour, minute] = now.split(':').map(Number);
  let period = 'Period1';
  if ((hour === 8 && minute >= 30) || (hour === 9 && minute < 45)) {
    period = 'Period1';
    window.location.href='{{url_for("classPeriod",period="Period1")}}'
  } else if ((hour === 9 && minute >= 45) || (hour === 11 && minute < 25)) {
    period = 'Period2';
    window.location.href='{{url_for("classPeriod",period="Period1")}}'
  } else if ((hour === 11 && minute >= 25) || (hour === 13 && minute < 30)) {
    period = 'Period3';
    window.location.href='{{url_for("classPeriod",period="Period1")}}'
  } else if ((hour === 13 && minute >= 30) || (hour === 15 && minute < 10)) {
    period = 'Period4';
    window.location.href='{{url_for("classPeriod",period="Period1")}}'
  } else if ((hour === 15 && minute >= 10) || (hour === 16 && minute < 10)) {
    period = 'Period8';
    window.location.href='{{url_for("classPeriod",period="Period1")}}'
  }
  return period
}
