import day7.DirectoryNode;
import day7.FileSystem;

public class Day7 extends Day{
    FileSystem fileSystem;

    public Day7(Type type){
        super(7, type);
        this.fileSystem = new FileSystem();
        for(int i = 0; i<this.strings.size(); i++){
            String line = this.strings.get(i);
            String[] parts = line.split(" ");
            switch (parts[0]) {
                case "$" -> {
                    switch (parts[1]) {
                        case "cd":
                            fileSystem.cd(parts[2]);
                        case "ls":
                            break;
                        default:
                            System.out.println("command unknown" + parts[1]);
                    }
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
        return this.fileSystem.findDirectoryToDelete();
    }
}
