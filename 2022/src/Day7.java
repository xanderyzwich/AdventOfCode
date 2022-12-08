import day7.FileSystem;

public class Day7 extends Day{
    FileSystem fileSystem;

    public Day7(Type type){
        super(7, type);
        this.fileSystem = new FileSystem();
        for (String line : this.strings) {
            String[] parts = line.split(" ");
            switch (parts[0]) {
                case "$" -> {
                    if (parts[1].equals("cd")) // ls requires nothing to be done
                        fileSystem.cd(parts[2]);
                }
                case "dir" -> fileSystem.addDirectory(parts[1]);
                default -> fileSystem.addFile(parts[1], Integer.parseInt(parts[0]));
            }
        }
    }


    public Integer part1() {
        int maximumSize = 100000;
        return this.fileSystem.findDirectoriesLargerThanSize(maximumSize);
    }

    public Integer part2() {
        int neededSpace = 30000000;
        return this.fileSystem.findSmallestDirectoryLargerThanSize(neededSpace);
    }
}
