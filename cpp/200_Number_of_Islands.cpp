/*
date: 200929
idea: 
1. DFS: recursion to search all of the neighbors which is '1'
- write dfs function to set all the '1' neighbors of (grid[r][c]==1) to '0'. 
- traverse all elements by dfs. increase island_nums if there is a '1'.

S2. BFS: use queue to search all neighbors of one element and then to search other element neighbors.
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

class Solution2 {
public:
    int numIslands(vector<vector<char>>& grid) {
        int nr = grid.size();
        if(!nr) return 0;
        int nc = grid[0].size();

        int islands_num = 0;

        for(int r=0; r<nr; r++){
            for(int c=0; c<nc; c++){
                if(grid[r][c] == '1'){
                    islands_num++;
                    grid[r][c] = '0';
                    queue<pair<int, int>> neighbors;
                    neighbors.push({r, c});

                    while(!neighbors.empty()){
                        auto rc = neighbors.front();
                        neighbors.pop();
                        int row = rc.first;
                        int col = rc.second;

                        if(row-1>=0 && grid[row-1][col] == '1'){
                            grid[row-1][col] = '0';
                            neighbors.push({row-1, col});
                        } 
                        if(row+1<nr && grid[row+1][col] == '1'){
                            grid[row+1][col] = '0';
                            neighbors.push({row+1, col});
                        }
                        if(col-1>=0 && grid[row][col-1] == '1'){
                            grid[row][col-1] = '0';
                            neighbors.push({row, col-1});
                        }
                        if(col+1<nc && grid[row][col+1] == '1'){
                            grid[row][col+1] = '0';
                            neighbors.push({row, col+1});
                        }
                    }
                }
            }
        }
        return islands_num;
    }
};
