import java.io.*;
import java.util.*;

public class DFS_maze {
    public static int N, M;
    public static int[][] graph = new int[200][200];
    // 이동할 네 가지 방향 정의 {상, 하, 좌 ,우}
    public static int dx[] = { -1, 1, 0, 0 };
    public static int dy[] = { 0, 0, -1, 1 };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // N, M 입력
        N = scanner.nextInt();
        M = scanner.nextInt();
        scanner.nextLine(); // 버퍼 지우기
        System.out.println("n " + N + "m" + M);
        // 2차원 배열의 정보 입력 받기
        for (int i = 0; i < N; i++) {
            String str = scanner.nextLine();
            for (int j = 0; j < M; j++) {
                graph[i][j] = str.charAt(j) - '0';
            }
        }
        scanner.close();
        System.out.println("result = " + dfs(0, 0));
    }

    private static int dfs(int x, int y) {
        Stack<Node> stack = new Stack<Node>();
        Node node = new Node(x, y);
        stack.push(node);
        while (!stack.empty()) {
            node = stack.pop();
            x = node.getX();
            y = node.getY();
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                // 미로 범위를 벗어나면 무시
                if (nx < 0 || ny < 0 || nx >= N || ny >= M)
                    continue;
                // 한 번 왔던 위치면 무시 , 괴물이 있는 위치면 무시
                if (graph[nx][ny] == 1) {
                    System.out.println("[" + nx + "," + ny + "]");
                    graph[nx][ny] = graph[x][y] + 1;
                    stack.push(new Node(nx, ny));
                }
            }
        }
        return graph[N - 1][M - 1];
    }

    static class Node {
        final private int x;
        final private int y;

        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }
    }
}
