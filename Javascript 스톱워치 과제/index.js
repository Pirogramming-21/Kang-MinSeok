let seconds = 0;      // seconds
let centiseconds = 0; // 1/100 seconds
let spanSeconds = document.getElementById('sec');
let spanCentiseconds = document.getElementById('msec');
let buttonStart = document.getElementById('btn-start');
let buttonStop = document.getElementById('btn-stop');
let buttonReset = document.getElementById('btn-reset');
let interval;  // 1/100 초씩 자동실행되는 곳에 사용할 변수
let recordList = document.querySelector('.record-list');
let buttonDelete = document.getElementById('btn-delete');
let checkAll = document.getElementById('check-all');
function getRecordCheckboxes() {
    return recordList.querySelectorAll('.record-check'); // 기록 목록 내의 체크박스 선택
}

// 시작버튼 누를시 실행함수
buttonStart.onclick = function() {
  if(buttonStart.disabled == false) {     // start버튼이 활성화 되었다면(여러번 실행되는 것 방지)
    interval = setInterval(startTimer, 10); // startTimer함수를 10/1000초마다 실행하겠다.
  }
}
 
// 정지버튼을 누를시 실행함수
buttonStop.onclick = function() {
  clearInterval(interval); // 1/100초마다 실행되는 함수 멈춤
  buttonStart.disabled = false; // start 버튼을 활성화 하기

  let recordItem = document.createElement('li');
  let recordContent = document.createElement('div');
  recordContent.classList.add('record-content');
  
  let recordCheckbox = document.createElement('input');
  recordCheckbox.type = 'checkbox';
  recordCheckbox.classList.add('record-check');
  
  let recordTime = document.createElement('span');
  recordTime.textContent = `${spanSeconds.innerText} : ${spanCentiseconds.innerText}`;
  
  recordContent.appendChild(recordCheckbox);
  recordContent.appendChild(recordTime);
  recordItem.appendChild(recordContent);
  
  // 새로운 기록을 목록에 추가
  recordList.appendChild(recordItem);
}
 
// 재시작 버튼 누를시 실행함수
buttonReset.onclick = function() {
  buttonStart.disabled == false;  // start 버튼을 활성화하기
  clearInterval(interval); // 1/100초마다 실행되는 함수 멈춤
  centiseconds = 0;
  seconds = 0;
  spanCentiseconds.innerText = '00';
  spanSeconds.innerText = '00';
}
 
// 삭제 버튼 클릭 시 체크된 항목만 삭제
buttonDelete.addEventListener('click', function() {
    // 모든 체크박스 요소를 가져와서
    let checkboxes = recordList.querySelectorAll('.record-check');
    
    checkboxes.forEach(function(checkbox) {
        if (checkbox.checked) { // 체크된 항목만
            let listItem = checkbox.closest('li'); // 체크박스가 포함된 <li> 요소를 찾음
            if (listItem) {
                listItem.remove(); // <li> 요소를 삭제
            }
        }
    });
});

function startTimer() { // 1초, 2초......시간 계산하는 함수
  centiseconds++;  // 1증가 // centiseconds = centiseconds + 1
  if(centiseconds <= 9) spanCentiseconds.innerText = '0'+centiseconds;
  else spanCentiseconds.innerText = centiseconds;
 
  if(centiseconds > 99) {
    seconds++; // 1초 상승
    if(seconds <= 9) spanSeconds.innerText = '0' + seconds;
    else spanSeconds.innerText = seconds;
    centiseconds = 0;
    spanCentiseconds.innerText = '00';
  }
}
// 전체 선택 체크박스 클릭 시 모든 체크박스 상태 변경
checkAll.addEventListener('change', function() {
    let isChecked = this.checked; // 전체 선택 체크박스의 체크 상태
    let recordCheckboxes = getRecordCheckboxes(); // 모든 기록 체크박스 재선택
    recordCheckboxes.forEach(function(checkbox) {
        checkbox.checked = isChecked; // 각 체크박스의 상태를 전체 선택 체크박스의 상태로 설정
    });
});