window.onload = function () {
  var userAgent = window.navigator.userAgent.toLowerCase();
  if(userAgent.indexOf('msie') !== -1 || userAgent.indexOf('trident') !== -1){
    alert('お使いのブラウザ(Internet Explorer)は動作対象外です。つまり、お使いのブラウザではこのサイトを正常に利用することはできません。FirefoxかChrome系(Chromium)のブラウザは動作対象確認済みですので、そちらの利用をおすすめします。')
  };
}

window.onload = function() {
  const spinner = document.getElementById('loading');
  spinner.classList.add('loaded');
}

function broke(){
  const spinner2 = document.getElementById('loading');
  spinner2.classList.add('loaded');
}
