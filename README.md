# sentence_tramsformer_api


## Docker Build

### Clone repo

```bash
git clone https://github.com/gomgomcode/sentence_tramsformer_api
```

### build

```bash
cd sentence_tramsformer_api
docker build --tag sentence_transformer_api:0.1 .
```

### run

```bash
docker run --gpus all --shm-size=16g -it -v /input_local_path/sentence_transformer_api/app:/app --rm -p 4004:4004 sentence_transformer_api:0.1
```

port 4004번으로 세팅되어 있으므로 필요시 도커파일 및 실행 명령어에서 포트 변경

### get embedding

/embedding 으로 post 요청