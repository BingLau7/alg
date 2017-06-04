package io.github.binglau.unkown;

import java.util.Random;
import java.util.concurrent.LinkedBlockingQueue;

/**
 * 文件描述: BlackQueue 生产者消费者
 */

public class ProducerAndConsumer {
    private final int MAX_SIZE = 100;
    private LinkedBlockingQueue<Integer> queue = new LinkedBlockingQueue<>(MAX_SIZE);
    private Random random = new Random();

    public void produce(int num) {
        if (queue.size() == MAX_SIZE) {
            System.out.println("库存超出");
        }

        for (int i = 0; i < num; i++) {
            try {
                int a = random.nextInt();
                queue.put(a);
                System.out.println("加入产品: " + a);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("现库存为:" + queue.size());
        }
    }

    public void consume(int num) {
        if (queue.size() == 0) {
            System.out.println("库存不足");
        }

        for (int i = 0; i < num; i++) {
            try {
                int a = queue.take();
                System.out.println("取出产品: " + a);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("现余下库存为:" + queue.size());
        }
    }

    public static void main(String[] args) {
        ProducerAndConsumer storage = new ProducerAndConsumer();

        Producer p1 = new Producer(storage, 10);
        Producer p2 = new Producer(storage, 2);
        Producer p3 = new Producer(storage, 5);

        Consumer c1 = new Consumer(storage, 3);

        new Thread(c1).start();
        new Thread(p1).start();
        new Thread(p2).start();
        new Thread(p3).start();
    }
}

class Producer implements Runnable {
    private ProducerAndConsumer storage;
    private int nums;

    public Producer(ProducerAndConsumer storage, int nums) {
        this.storage = storage;
        this.nums = nums;
    }

    @Override
    public void run() {
        storage.produce(nums);
    }
}

class Consumer implements Runnable {
    private ProducerAndConsumer storage;
    private int nums;

    public Consumer(ProducerAndConsumer storage, int nums) {
        this.storage = storage;
        this.nums = nums;
    }

    @Override
    public void run() {
        storage.consume(nums);
    }
}
