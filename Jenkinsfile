pipeline {
    agent any
    environment {
        PYTHON = 'C:/Users/Admin/AppData/Local/Programs/Python/Python312/python.exe'
    }
    stages {
        stage('Setup') {
            steps {
                bat '"%PYTHON%" -m venv .venv'
                bat '.venv\\Scripts\\python -m pip install -r requirements.txt pytest'
            }
        }
        stage('Test') {
            steps {
                bat '.venv\\Scripts\\python -m pytest -v --junitxml=results.xml'
            }
            post {
                always { junit 'results.xml' }
            }
        }
        stage('Smoke Test') {
            steps {
                powershell '''
                    $app = Start-Process -FilePath ".venv/Scripts/python.exe" -ArgumentList "-m streamlit run app.py --server.headless true --server.address 127.0.0.1 --server.port 8501" -PassThru -WindowStyle Hidden
                    try {
                        curl.exe --fail --retry 15 --retry-delay 2 --retry-connrefused http://127.0.0.1:8501/_stcore/health
                        if ($LASTEXITCODE -ne 0) { throw "App did not start" }
                    } finally {
                        taskkill /PID $app.Id /T /F
                    }
                '''
            }
        }
    }
}
