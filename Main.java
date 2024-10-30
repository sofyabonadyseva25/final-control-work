public class Main {
    public static void main(String[] args) {
        ToyStore store = new ToyStore();
        
        // Добавляем игрушки в очередь
        store.addToy(new Toy(1, "Teddy Bear", 5));
        store.addToy(new Toy(2, "Robot", 10));
        store.addToy(new Toy(3, "Lego Set", 8));
        store.addToy(new Toy(4, "Puzzle", 3));
        store.addToy(new Toy(5, "Doll", 6));

        // Проводим розыгрыш и записываем результат в файл
        store.drawToys(10, "draw_results.txt");

        System.out.println("Draw results saved in 'draw_results.txt'");
    }
}

