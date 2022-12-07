import day7.DirectoryNode;
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
        return this.fileSystem.listDirectories()
                .stream().map(DirectoryNode::getSize)
                .filter(size -> 100000>= size)
                .reduce(0, Integer::sum);
    }

    public Integer part2() {
        int neededSpace = 30000000;
        return this.fileSystem.findDirectoryToDelete(neededSpace);
    }
}
