class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int tem=x;
        int rv=0;
        while(x>0){
           int d=x%10;
           rv =rv*10+d;
           x=x/10;
        }
        return rv==tem;
    }
}