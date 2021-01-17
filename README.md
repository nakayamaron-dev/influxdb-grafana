# influxdb-grafana
influxdbとgrafanaをDockerでパパっと立ち上げる。

## 起動
- docker-composeで起動
```
docker-compose up -d (sudoが最初に必要な場合あり)
```

- influxdbにサンプルデータ投入 (sampleという名前のdatabaseが作られる。)  
必要なモジュールは[requirements.txt](/requirements.txt)を参照。
```
python write_sample_data.py
```

## 動作確認
ブラウザでgrafana(http://localhost:3000)にアクセス  
初期usernameとpasswordはadmin / admin (初回ログイン後、変更できる)
![grafana](images/grafana_login.png)

- Dashboard (sample)に投入したデータが表示される。

![dashboard](images/sample_dashboard.png)  

以上。
