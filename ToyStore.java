import java.io.FileWriter;
import java.io.IOException;
import java.util.PriorityQueue;
import java.util.Random;

public class ToyStore {
    private PriorityQueue<Toy> toyQueue;
    private Random random;

    public ToyStore() {
        this.toyQueue = new PriorityQueue<>((a, b) -> b.getWeight() - a.getWeight());
        this.random = new Random();
    }

    public void addToy(Toy toy) {
        toyQueue.add(toy);
    }

    public Toy getToy() {
        return toyQueue.poll();
    }

    public void drawToys(int times, String fileName) {
        try (FileWriter writer = new FileWriter(fileName)) {
            for (int i = 0; i < times; i++) {
                Toy toy = getToy();
                if (toy != null) {
                    writer.write("Toy ID: " + toy.getId() + ", Name: " + toy.getName() + "\n");
                    addToy(toy);
                }
            }
        } catch (IOException e) {
            System.out.println("Error writing to file: " + e.getMessage());
        }
    }
}
