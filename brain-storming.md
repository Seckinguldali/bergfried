## Brainstorming of the dataflow distribution logic

## 1. Task distribution logic among the nodes
- There will be tasks that need to be distributed among the nodes in the cluster. The distribution logic will be based on factors such as:
  - Node capacity (CPU, memory, etc.)
  - Task priority
  - Load balancing (to ensure that no single node is overwhelmed)

## Dataflow/Pipeline distribution logic among the nodes with Mermaid diagram

```mermaid
graph TD
    A[Node 1: Sensor collects data] --> B[Node 1: Data is preprocess before storing]
    B --> C[Node 1: Data stores in the node 1 storage]
    C --> D[Node 1 or 2: Data is send from node 1 storage to node 2 storage or Data is pulled from node 1 storage to node 2 storage]
    D --> E[Node 2: Data is preprocess before storing]
    E --> F[Node 2: Data stores in the node 2 storage]
    F --> G[Node 2: Data is send to node 3 for training]
    G --> H[Node 3: Data is preprocess before training]
    H --> I[Node 3: Model is trained using the data from node 2]


Node 1. Sensor collects data
Node 1. Data is preprocess before storing
Node 1. Data stores in the node 1 storage

    Node 1 or 2. Data is send from node 1 storage to node 2 storage or Data is pulled from node 1 storage to node 2 storage

Node 2. Data is preprocess before storing
Node 2. Data stores in the node 2 storage
Node 2. Data is send to node 3 for training
Node 3. Data is preprocess before training
Node 3. Model is trained using the data from node 2
Node 3. Trained model is stored in node 3 storage
Node 3. Trained model is send to node 4 for inference
Node 4. Trained model is preprocess before inference
Node 4. Inference is performed using the trained model from node 3
Node 4. Inference results are stored in node 4 storage
Node 4. Inference results are send to node 1 for further processing or visualization
Node 1. Inference results are preprocess before visualization
Node 1. Inference results are visualized for the end-users