// 클릭한 사진을 메인 프로필 사진으로 바꾸기
function changeMainPhoto(imgElem) {
  const mainPhoto = document.getElementById('main-photo');
  mainPhoto.src = imgElem.src;
}

// Footer 연도 자동 업데이트
document.getElementById('year').textContent = new Date().getFullYear();
