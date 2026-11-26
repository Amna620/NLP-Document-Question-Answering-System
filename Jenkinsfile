pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh '''
                    python3.12 -m venv .venv
                    .venv/bin/pip install torch==2.15.0 --index-url https://download.pytorch.org/whl/cpu
                    .venv/bin/pip install -r requirements.txt pytest
                '''
            }
        }
        stage('Test') {
            steps {
                sh '.venv/bin/python -m pytest -v --junitxml=results.xml'
            }
            post {
                always { junit 'results.xml' }
            }
        }
        stage('Smoke Test') {
            steps {
                sh '''
                    .venv/bin/python -m streamlit run app.py --server.headless true --server.address 127.0.0.1 --server.port 8501 &
                    APP_PID=$!
                    trap "kill $APP_PID" EXIT
                    curl --fail --retry 15 --retry-delay 2 --retry-connrefused http://127.0.0.1:8501/_stcore/health
                '''
            }
        }
    }
}
