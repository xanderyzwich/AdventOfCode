package day7;

import lombok.Getter;

import java.util.*;

@Getter
public class DirectoryNode extends FileSystemNode{

    // members
    private final Map<String, FileSystemNode> children;
    private final DirectoryNode parent;

    // Constructors
    DirectoryNode(String name, DirectoryNode parent){
        super(name);
        this.parent = parent;
        this.children = new HashMap<>();
    }

    DirectoryNode(String name){
        this(name, null);
    }

    // Accessors
    @Override
    public Integer getSize() {
        return children.values().stream()
                .map(FileSystemNode::getSize)
                .reduce(0, Integer::sum);
    }

    List<DirectoryNode> getDirectoryList(){
        List<DirectoryNode> directoryNodeList = new LinkedList<>();
        directoryNodeList.add(this);
        this.children.values().stream()
                .filter(fileSystemNode -> fileSystemNode instanceof DirectoryNode)
                .map(dn -> (DirectoryNode)dn)
                .forEach(directoryNode -> directoryNodeList.addAll(directoryNode.getDirectoryList()));
        return directoryNodeList;
    }

    public String toString(){
        return String.format("%s: %s", this.getName(), this.getSize());
    }

    // Mutators
    void addChild(FileSystemNode child){
        children.put(child.getName(), child);
    }
}
