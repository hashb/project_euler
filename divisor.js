<script> 
msTotal = [0,0,0,0,0,0,0,0,0,0,0];
msAvg   = [0,0,0,0,0,0,0,0,0,0,0];
nRuns   = [0,0,0,0,0,0,0,0,0,0,0];
bExForm = 0;

function formatTime(nn) {
 var hh = Math.floor(nn/3600000);
 var mm = Math.floor(nn/60000) - 60*hh;
 var ss = Math.floor(nn/1000) - 3600*hh - 60*mm;
 var ms = nn - 3600000*hh - 60000*mm - 1000*ss;
 return (''+(100 + hh)).substring(1)+
    ':'+(''+(100 + mm)).substring(1)+
    ':'+(''+(100 + ss)).substring(1)+
    '.'+(''+(1000+ ms)).substring(1)
}

function updateTiming(parDate,k) {
 var nn = (new Date())-parDate;
 msTotal[k] += nn;
 nRuns  [k] += 1;
 msAvg  [k] = Math.round(msTotal[k]/nRuns[k])

 if (document.forms[k].jsElapsed) document.forms[k].jsElapsed.value = formatTime(nn);
 if (document.forms[k].jsAverage) document.forms[k].jsAverage.value = formatTime(msAvg[k]);
 if (document.forms[k].pct!=null && msAvg[0]>0)
 { // percentages:
  for (var k=document.forms.length; k--; ) { //hee-hee
   document.forms[k].pct.value = (100*msAvg[k]/msAvg[0]).toFixed(1);
  }
 }
 return nn;
}

function divisibleBy(d,hi,lo) {return 0==((1000000000000000%d)*hi+lo)%d}

leastFactor_ = function(s) { 
 if (typeof(s)=='number') return leastFactor(s);
 if (typeof(s)!='string') return NaN;
 if (s.match(/\D/)) return NaN;

 var n = parseFloat(s);
 if (isNaN(n) || !isFinite(n)) return NaN;
 if (n<9007199254740992) return leastFactor(n);

 var lo=0, hi=0, len=s.length;

 if (len>20) return 'Exceeded the 20 digits maximum.'
 if (len>15) {
  lo = parseInt(s.substring(len-15), 10);
  hi = parseInt(s.substring(0,len-15), 10);
 }
 else lo=parseInt(s, 10);

 if (lo%2==0)               return 2;
 if (divisibleBy(3,hi,lo))  return 3;
 if (lo%5==0)               return 5;
 if (divisibleBy(7,hi,lo))  return 7;
 if (divisibleBy(11,hi,lo)) return 11;
 if (divisibleBy(13,hi,lo)) return 13;
 if (divisibleBy(17,hi,lo)) return 17;
 if (divisibleBy(19,hi,lo)) return 19;
 if (divisibleBy(23,hi,lo)) return 23;
 if (divisibleBy(29,hi,lo)) return 29;
 if (divisibleBy(31,hi,lo)) return 31;

 var m = Math.ceil(Math.sqrt(n)+0.5);

 // detect squares and near-squares early!
 for (var i=7+30*Math.floor(m/30-100);i<=m;i+=30) {
  if (divisibleBy(i,hi,lo))    return leastFactor(i);
  if (divisibleBy(i+4,hi,lo))  return leastFactor(i+4);
  if (divisibleBy(i+6,hi,lo))  return leastFactor(i+6);
  if (divisibleBy(i+10,hi,lo)) return leastFactor(i+10);
  if (divisibleBy(i+12,hi,lo)) return leastFactor(i+12);
  if (divisibleBy(i+16,hi,lo)) return leastFactor(i+16);
  if (divisibleBy(i+22,hi,lo)) return leastFactor(i+22);
  if (divisibleBy(i+24,hi,lo)) return leastFactor(i+24);
 }

 for (var i=37;i<=m;i+=30) {
  if (divisibleBy(i,hi,lo))    return i;
  if (divisibleBy(i+4,hi,lo))  return i+4;
  if (divisibleBy(i+6,hi,lo))  return i+6;
  if (divisibleBy(i+10,hi,lo)) return i+10;
  if (divisibleBy(i+12,hi,lo)) return i+12;
  if (divisibleBy(i+16,hi,lo)) return i+16;
  if (divisibleBy(i+22,hi,lo)) return i+22;
  if (divisibleBy(i+24,hi,lo)) return i+24;
 }
 return s;
}

function factor_(n) {
 var s = n.toString().replace(/^\s+|\s+$/g,'');
 var f=parseFloat(s), len=s.length;

 if (s=='' ) return 'Empty input'
 if (isNaN(f) || f%1 || s.match(/\D/))
   return 'Invalid input [expected a positive integer, digits only]'
 if (s.length>20 ) return 'Invalid input [exceeded the 20 digits maximum]'
 if (f<9007199254740992) return factor(parseInt(s,10));

 var lastDigit = parseInt(s.charAt(len-1),10);
 if (lastDigit==1 || lastDigit==3 || lastDigit==7 || lastDigit==9) {
  if (isPrimeMR15(s)) return s;
 }

 var minFactor = leastFactor_(s).toString();
 if (s==minFactor) return s;

 var x = str2bigInt(s,10,len);
 var y = str2bigInt(minFactor,10,len);
 var q = str2bigInt('1',10,len);
 var r = str2bigInt('1',10,len);

 divide_(x,y,q,r);
 return minFactor+'*'+factor_(bigInt2str(q,10));
}

function numericSortOrder(x,y) {return x-y;}

function factorSort(n) {
 var res = factor_(n);
 if (res.indexOf('*')==-1) return res;
 return res.split('*').sort(numericSortOrder).join('*');
}

function findDivisors(n) {
 var j=-1, f0=1, f1=1, nDivs=1, d=1, tmp=1, k=0, sum=0;
 var powers=[], distinctFactors=[], tmpow=[], divisors =[1];
 var res = factor_(n);

 if (res.indexOf('i')!=-1) return res;
 if (parseInt(n,10) < 2)   return '1 divisor: 1';
 if (res.indexOf('*')==-1) return '2 divisors: 1 '+res;

 var factors = res.split('*').sort(numericSortOrder);
 for (var i=0; i < factors.length; i++) {
  f0 = f1;  f1 = factors[i];
  if (f1 != f0) {	
   powers[++j] = 1;
   distinctFactors[j] = f1;
  }
  else powers[j]++;
 }

 var m=distinctFactors.length;
 for (var j=0; j < m; j++) {
  tmpow[j] = 0;
  nDivs = nDivs * (1+powers[j]);
 }
 while (divisors.length < nDivs) {
  k=0; d=1;
  while (++tmpow[k] > powers[k]) {
   tmpow[k]=0;
   k++;
  }
  for (var j=0; j < m; j++) {
   if (tmpow[j]) {
    if ((tmp=d*Math.pow(distinctFactors[j],tmpow[j]))<=9007199254740991) d=tmp;
    else { for (var i=0;i<tmpow[j];i++) d = multiplyBig(d,distinctFactors[j]);  }
   }
  }
  divisors[divisors.length] = d; //alert('tmpow ='+tmpow +'\ndivisors='+divisors );
 }
 divisors.sort(numericSortOrder);

 for (var i=0; i<divisors.length; i++) {
  if ((tmp=parseInt(sum,10)+parseInt(divisors[i],10))<=9007199254740991) sum = tmp;
  else sum = addBig(sum,divisors[i]);
 }

 return ''
  + 'Sum of divisors: ' + sum  + '.   '
  + nDivs+'\xA0divisors: \n'
  + divisors.join(' ');
}

function multiplyBig(x1,x2) {
 var s1 = x1.toString(), s2 = x2.toString();
 var len=Math.max(s1.length,s2.length);
 var b1 = str2bigInt(s1,10,len);
 var b2 = str2bigInt(s2,10,len);
 return bigInt2str ( mult(b1,b2) , 10 );
}

function addBig(x1,x2) {
 var s1 = x1.toString(), s2 = x2.toString();
 var len=Math.max(s1.length,s2.length);
 var b1 = str2bigInt(s1,10,len);
 var b2 = str2bigInt(s2,10,len);
 return bigInt2str ( add(b1,b2) , 10 );
}

if (typeof one  == 'undefined') one  = int2bigInt(1,1,1);
if (typeof zero == 'undefined') zero = int2bigInt(0,1,1);

// mrr3 takes BigInt a, i, n

function mrr3(a, i, n) {
  if (isZero(i)) return one;

  //  j = floor(i/2)
  var j = dup(i); divInt_(j,2);   
  var x = mrr3(a, j, n);    
  if (isZero(x)) return zero;
 
  //  y = (x*x)%n
  var y = expand(x,n.length); squareMod_(y,n);
  if (equalsInt(y,1) && !equalsInt(x,1) && !equals(x, addInt(n,-1)) ) return zero; 
  if (i[0]%2==1) multMod_(y,a,n);
  return y;
}

function miller_rabin(n,a) {
 var s = n.toString(); 
 var res, len=s.length;
 var mr_base = str2bigInt(a.toString(),10,len);
 var mr_cand = str2bigInt(s,10,len);
 var mr_temp = addInt(mr_cand,-1)

 res = mrr3 (mr_base, mr_temp, mr_cand);
 if ((typeof res=='object') && equalsInt(res,1) ) return 1;
 return 0;
}

smallPrimes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113];

function isPrimeMR15(n) {
 var a, s = n.toString(); 
 for (var k=0;k<15;k++) {
  a = smallPrimes[k];
  if (s==''+a) return 1;
  if (miller_rabin(s,a)==0) return 0;
 }
 return 1;
}

//--> 
</script>