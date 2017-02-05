r=1;
sidelen=1;
nums=1;
primenums=0;
while r>0.1
    sidelen = sidelen +2;
    diagValues = [((sidelen-1)^2 - (sidelen-2)), (sidelen-1)^2 + 1, (sidelen-1)^2 + sidelen, sidelen*sidelen];
    nums = nums+4;
    primenums = primenums + sum(isprime(diagValues));
    r = primenums/nums;
end
sidelen