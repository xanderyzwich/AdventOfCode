package day7;

import java.util.List;

public class FileSystem {
    private DirectoryNode root;
    private DirectoryNode current;

    public FileSystem(){
        this.root = new DirectoryNode("/");
        this.current = this.root;
    }

    public void cd(String destination){
        String where = destination.equals("..") ? "up to " +this.current.parent.name : destination;
//        System.out.printf("Changing Directory %s%n", where);
        switch (destination) {
            case ".." -> this.current = current == root ? root : current.parent;
            case "/" -> this.current = this.root;
            default -> this.current = (DirectoryNode) this.current.children.get(destination);
        }
    }

    public void addFile(String name, Integer size){
        String here = this.current.name.equals("/") ? "" : this.current.name;
//        System.out.printf("Adding file %s/%s: %s%n", here, name, size);
        this.current.addChild(new FileNode(name, size));
    }

    public void addDirectory(String name){
        String here = this.current.name.equals("/") ? "" : this.current.name;
//        System.out.printf("Adding directory %s/%s%n", here, name);
        this.current.addChild(new DirectoryNode(name, this.current));
    }

    public List<DirectoryNode> listDirectories(){
        List<DirectoryNode> directoryList = this.root.getDirectoryList();
//        System.out.println(directoryList);
        return directoryList;
    }

}
