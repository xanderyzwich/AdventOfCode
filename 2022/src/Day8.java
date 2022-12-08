import util.ArrayTools;

import java.util.Arrays;

public class Day8 extends Day{
    int[][] treeHeights;

    public Day8(Type type){
        super(8, type);
        // create 2d int array for tree heights
        int rows = this.strings.size();
        int cols = this.strings.get(0).length();
        treeHeights = new int[rows][cols];
        for(int i=0; i<this.strings.size(); i++){
            String[] row = this.strings.get(i).split("");
            for(int j=0; j<row.length; j++){
                this.treeHeights[i][j] = Integer.parseInt(row[j]);
            }
        }

    }

    public Integer part1(){
        // top/bottom + left/right - corners
        int height = treeHeights.length;
        int width = treeHeights[0].length;
        int visibleCount = (2*height) + (2*width) - 4;

        // iterate interior trees
        for(int i=1; i<height-1; i++){
            for(int j=1; j<width-1; j++){
//                visibleCount += isVisible(i,j) ? 1 : 0;
                visibleCount += isVisibleWithSlice(i,j) ? 1 : 0;
            }
        }
        return visibleCount;
    }

    /*
    Original implementation
    I didn't like how much duplicated looping there was
     */
    public boolean isVisible(int row, int col){
        int currentHeight = this.treeHeights[row][col];
        int visibleDirections = 4;

        // check up
        for(int i=0; i<row; i++){
            int checkHeight = this.treeHeights[i][col];
            if(checkHeight >= currentHeight){
//                System.out.printf("UP: Checking if %s blocks %s%n", checkHeight, currentHeight);
                visibleDirections--;
                break;
            }
        }

        // check down
        for(int i=row+1; i<this.treeHeights.length; i++){
            int checkHeight = this.treeHeights[i][col];
            if(checkHeight >= currentHeight){
//                System.out.printf("DOWN: Checking if %s blocks %s%n", checkHeight, currentHeight);
                visibleDirections--;
                break;
            }
        }

        // check left
        for(int j=0; j<col; j++){
            int checkHeight = this.treeHeights[row][j];
            if(checkHeight >= currentHeight){
//                System.out.printf("LEFT: Checking if %s blocks %s%n", checkHeight, currentHeight);
                visibleDirections--;
                break;
            }
        }

        // check right
        for(int j=col+1; j<treeHeights[row].length; j++){
            int checkHeight = this.treeHeights[row][j];
            if(checkHeight >= currentHeight) {
//                System.out.printf("RIGHT: Checking if %s blocks %s%n", checkHeight, currentHeight);
                visibleDirections--;
                break;
            }
        }

        return visibleDirections > 0;
    }

    /*
    Updated implementation using slices
     */
    public boolean isVisibleWithSlice(int row, int col){
        int currentHeight = this.treeHeights[row][col];
        int[][] slices = ArrayTools.sliceAllDirections(this.treeHeights, row, col);
        int visibleDirections = 4;

        // iterate directions
        for(int[] slice : slices){
            for(int i : slice){
                if(i>=currentHeight){
                    visibleDirections--;
                    break;
                }
            }
        }
        return visibleDirections > 0;
    }

    public Integer part2(){
        int maxScenicScore = 0;
        // iterating interior trees
        for(int i =1; i<this.treeHeights.length-1; i++){
            for(int j=1; j<this.treeHeights[i].length; j++){
//                int currentScore = this.getScenicScore(i,j);
                int currentScore = this.getScenicScoreWithSlices(i,j);
                if (currentScore>maxScenicScore)
                    maxScenicScore = currentScore;
            }
        }
        return maxScenicScore;
    }

    /*
    Original implementation
    I didn't like how much duplicated looping there was
     */
    public int getScenicScore(int row, int col){
        int currentHeight = this.treeHeights[row][col];

        // check up
        int upScore = 0;
        for(int i=row-1; i>=0; i--){
            upScore++;
            if(this.treeHeights[i][col]>=currentHeight)
                break;
        }

        // check down
        int downScore = 0;
        for(int i=row+1; i<this.treeHeights.length; i++){
            downScore++;
            if(this.treeHeights[i][col]>=currentHeight)
                break;
        }

        // check left
        int leftScore = 0;
        for(int j=col-1; j>=0; j--){
            leftScore++;
            if(this.treeHeights[row][j]>=currentHeight)
                break;
        }

        // check right
        int rightScore = 0;
        for(int j=col+1; j<this.treeHeights[row].length; j++){
            rightScore++;
            if(this.treeHeights[row][j]>=currentHeight)
                break;
        }

        return upScore * downScore * leftScore * rightScore;
    }

    /*
    Updated implementation using slices
     */
    public int getScenicScoreWithSlices(int row, int col){
        int currentHeight = this.treeHeights[row][col];
        int[][] slices = ArrayTools.sliceAllDirections(this.treeHeights, row, col);
        int[] directionScores = new int[slices.length];
        for(int i =0; i<slices.length; i++){
            int[] slice = slices[i];
            int directionScore = 0;
            for (int j : slice) {
                directionScore++;
                if (j >= currentHeight)
                    break;
            }
            directionScores[i] = directionScore;
        }
        return Arrays.stream(directionScores).reduce(1, (a, b)->a*b);
    }
}
