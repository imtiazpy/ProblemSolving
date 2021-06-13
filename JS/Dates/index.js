// Given a date string, "dateString", in the format MM/DD/YYYY, find and return the day name for that date. 
// Each day name must be one of the following strings: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday. 
// For example, the day name for the date 12/07/2016 is Wednesday.



function getDayName(dateString) {
    const date = new Date(dateString);

    const options = {
      weekday: 'long'
    };
  
    return new Intl.DateTimeFormat('en-Us', options).format(date);
}


function main() {
  const d = +(readLine());
  
  for (let i = 0; i < d; i++) {
      const date = readLine();
      
      console.log(getDayName(date));
  }
}

