/*
date: 200929
idea: 
1. DFS: recursion to search all of the neighbors which is '1'
- write dfs function to set all the '1' neighbors of (grid[r][c]==1) to '0'. 
- traverse all elements by dfs. increase island_nums if there is a '1'.
*/

class Solution {
    void dfs(vector<vector<char>>& grid, int r, int c){
        int nr = grid.size();
        int nc = grid[0].size();

        grid[r][c] = '0';

        if(r-1>=0 && grid[r-1][c] == '1') dfs(grid, r-1, c);
        if(r+1<nr && grid[r+1][c] == '1') dfs(grid, r+1, c);
        if(c-1>=0 && grid[r][c-1] == '1') dfs(grid, r, c-1);
        if(c+1<nc && grid[r][c+1] == '1') dfs(grid, r, c+1);
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        int nr = grid.size();
        if(!nr) return 0;
        int nc = grid[0].size();

        int island_nums = 0;

        for(int r=0; r<nr; r++){
            for(int c=0; c<nc; c++){
                if(grid[r][c] == '1'){
                    island_nums++;
                    dfs(grid, r, c);
                }
            }
        }
        return island_nums;
    }
};
