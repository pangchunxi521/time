function tz(n){
      return (n<10)?'0'+n:''+n
  };

  (function Rtime(){
      var nowTime = new Date;
      var endTime = new Date('2022/2/1 00:00:00');

      var t = endTime.getTime()  - nowTime.getTime() ;
      //alert(t)  //
      if(t>=0){
          var d = Math.floor(t/1000/60/60/24),
              h = Math.floor(t/1000/60/60%24),
              m = Math.floor(t/1000/60%60),
              s = Math.floor(t/1000%60)
      };

       setInterval(Rtime,1000);

       footer.innerHTML = '&copy <span class="time">探针小站</span> | 距离过年还有<span class="times">'+tz(d)+'</span>天<span class="time1">'+tz(h)+'</span>时<span class="time2">'+tz(m)+'</span>分<span class="time3">'+tz(s)+'</span>秒';;

  })()


