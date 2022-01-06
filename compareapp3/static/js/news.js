function randomcolor(){
    letters='0123456789ABCDEF'
    color="#"
    for (var i=0;i<6;i++){
      var r=Math.floor(Math.random()*16)
      color=color+letters[r]
    }
    return color
  }
  function change(){
  //var god=document.querySelector('.xxx');
  //god.style.background=randomcolor()
  var brand=document.querySelector('#change');
  brand.style.color=randomcolor()
  /*
  var detail=document.querySelector('.detail');
  detail.style.color=randomcolor()
  var detail1=document.querySelector('.detail1');
  detail1.style.color=randomcolor() */
  //var brand=document.querySelector('#thebrand')
  //brand.style.background=randomcolor()
  }
  setInterval(change,2000)
  