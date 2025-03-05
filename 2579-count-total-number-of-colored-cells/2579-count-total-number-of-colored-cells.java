class Solution {
    public long coloredCells(int n) {
        long N = n; 
        return (N * N) + ((N - 1) * (N - 1));
    }
}
