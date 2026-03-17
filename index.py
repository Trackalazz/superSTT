
html_code = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Speech-to-Text Pro</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            width: 100%;
            max-width: 800px;
            padding: 40px;
            backdrop-filter: blur(10px);
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
        }

        .header h1 {
            font-size: 2.5rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }

        .header p {
            color: #6b7280;
            font-size: 1.1rem;
        }

        .status-bar {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-bottom: 25px;
            padding: 12px 24px;
            background: #f3f4f6;
            border-radius: 50px;
            font-weight: 500;
        }

        .status-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #9ca3af;
            transition: all 0.3s ease;
        }

        .status-indicator.recording {
            background: #ef4444;
            animation: pulse 1.5s infinite;
        }

        .status-indicator.active {
            background: #10b981;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
        }

        .controls {
            display: flex;
            gap: 12px;
            margin-bottom: 25px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .btn {
            padding: 14px 28px;
            border: none;
            border-radius: 12px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }

        .btn:active {
            transform: translateY(0);
        }

        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .btn-danger {
            background: #ef4444;
            color: white;
        }

        .btn-success {
            background: #10b981;
            color: white;
        }

        .btn-warning {
            background: #f59e0b;
            color: white;
        }

        .btn-secondary {
            background: #6b7280;
            color: white;
        }

        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }

        .text-container {
            position: relative;
            margin-bottom: 20px;
        }

        .text-box {
            width: 100%;
            min-height: 300px;
            max-height: 500px;
            padding: 24px;
            border: 2px solid #e5e7eb;
            border-radius: 16px;
            font-size: 1.2rem;
            line-height: 1.8;
            resize: vertical;
            overflow-y: auto;
            background: #fafafa;
            transition: border-color 0.3s ease;
            font-family: 'Georgia', serif;
        }

        .text-box:focus {
            outline: none;
            border-color: #667eea;
            background: white;
        }

        .text-box.recording-active {
            border-color: #ef4444;
            background: #fff5f5;
        }

        .info-panel {
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 20px;
        }

        .info-panel h3 {
            color: #0369a1;
            margin-bottom: 12px;
            font-size: 1.1rem;
        }

        .commands-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            font-size: 0.9rem;
        }

        .command-item {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 6px 12px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        .command-key {
            font-weight: 600;
            color: #667eea;
        }

        .command-value {
            color: #374151;
            font-family: monospace;
            font-size: 1.1rem;
        }

        .stats {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-top: 20px;
            flex-wrap: wrap;
        }

        .stat-item {
            text-align: center;
            padding: 12px 24px;
            background: #f3f4f6;
            border-radius: 12px;
        }

        .stat-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: #667eea;
        }

        .stat-label {
            font-size: 0.875rem;
            color: #6b7280;
        }

        .permission-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.8);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            backdrop-filter: blur(5px);
        }

        .permission-modal {
            background: white;
            padding: 40px;
            border-radius: 24px;
            text-align: center;
            max-width: 500px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        }

        .permission-modal h2 {
            margin-bottom: 16px;
            color: #1f2937;
        }

        .permission-modal p {
            color: #6b7280;
            margin-bottom: 24px;
            line-height: 1.6;
        }

        .hidden {
            display: none !important;
        }

        .toast {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(100px);
            background: #1f2937;
            color: white;
            padding: 16px 32px;
            border-radius: 12px;
            font-weight: 500;
            opacity: 0;
            transition: all 0.3s ease;
            z-index: 1001;
        }

        .toast.show {
            transform: translateX(-50%) translateY(0);
            opacity: 1;
        }

        .interim-text {
            color: #9ca3af;
            font-style: italic;
        }

        @media (max-width: 640px) {
            .container {
                padding: 24px;
            }
            
            .header h1 {
                font-size: 1.8rem;
            }
            
            .controls {
                flex-direction: column;
            }
            
            .btn {
                width: 100%;
                justify-content: center;
            }
        }
    </style>
</head>
<body>
    <div id="permissionOverlay" class="permission-overlay">
        <div class="permission-modal">
            <div style="font-size: 3rem; margin-bottom: 16px;">🎙️</div>
            <h2>Permiso de Micrófono Requerido</h2>
            <p>Esta aplicación necesita acceder a tu micrófono para convertir tu voz en texto. 
               Por favor, haz clic en "Habilitar Micrófono" y permite el acceso cuando tu navegador lo solicite.</p>
            <button class="btn btn-primary" onclick="requestMicrophonePermission()">
                🎤 Habilitar Micrófono
            </button>
        </div>
    </div>

    <div class="container">
        <div class="header">
            <h1>🎙️ Speech-to-Text Pro</h1>
            <p>Dicta naturalmente, nosotros añadimos la puntuación</p>
        </div>

        <div class="status-bar">
            <div id="statusIndicator" class="status-indicator"></div>
            <span id="statusText">Listo para grabar</span>
        </div>

        <div class="controls">
            <button id="btnToggle" class="btn btn-primary" onclick="toggleRecording()">
                ▶️ Iniciar Grabación
            </button>
            <button id="btnStop" class="btn btn-danger" onclick="stopRecording()" disabled>
                ⏹️ Detener
            </button>
            <button id="btnCopy" class="btn btn-success" onclick="copyText()">
                📋 Copiar Texto
            </button>
            <button id="btnClear" class="btn btn-warning" onclick="clearText()">
                🗑️ Limpiar
            </button>
        </div>

        <div class="text-container">
            <textarea 
                id="textOutput" 
                class="text-box" 
                placeholder="El texto aparecerá aquí..."
                spellcheck="false"
            ></textarea>
        </div>

        <div class="info-panel">
            <h3>📖 Comandos de Puntuación por Voz</h3>
            <div class="commands-grid">
                <div class="command-item">
                    <span class="command-key">"coma"</span>
                    <span class="command-value">,</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"punto"</span>
                    <span class="command-value">.</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"punto y coma"</span>
                    <span class="command-value">;</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"dos puntos"</span>
                    <span class="command-value">:</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"raya" / "guion largo"</span>
                    <span class="command-value">—</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"abre interrogación"</span>
                    <span class="command-value">¿</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"cierra interrogación"</span>
                    <span class="command-value">?</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"abre exclamación"</span>
                    <span class="command-value">¡</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"cierra exclamación"</span>
                    <span class="command-value">!</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"paréntesis abierto"</span>
                    <span class="command-value">(</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"paréntesis cerrado"</span>
                    <span class="command-value">)</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"comillas" / "entre comillas"</span>
                    <span class="command-value">" "</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"salto de línea" / "nueva línea"</span>
                    <span class="command-value">↵</span>
                </div>
                <div class="command-item">
                    <span class="command-key">"punto y aparte"</span>
                    <span class="command-value">. + ↵</span>
                </div>
            </div>
        </div>

        <div class="stats">
            <div class="stat-item">
                <div id="wordCount" class="stat-value">0</div>
                <div class="stat-label">Palabras</div>
            </div>
            <div class="stat-item">
                <div id="charCount" class="stat-value">0</div>
                <div class="stat-label">Caracteres</div>
            </div>
            <div class="stat-item">
                <div id="timeCount" class="stat-value">00:00</div>
                <div class="stat-label">Duración</div>
            </div>
        </div>
    </div>

    <div id="toast" class="toast"></div>

    <script>
        // Variables globales
        let recognition = null;
        let isRecording = false;
        let isPaused = false;
        let finalTranscript = '';
        let interimTranscript = '';
        let recordingStartTime = null;
        let timerInterval = null;
        let audioContext = null;
        let microphoneStream = null;

        // Mapeo de comandos de puntuación
        const punctuationMap = {
            'coma': ',',
            'coma,': ',',
            'punto': '.',
            'punto.': '.',
            'punto y coma': ';',
            'punto y coma;': ';',
            'dos puntos': ':',
            'dos puntos:': ':',
            'raya': '—',
            'guion largo': '—',
            'abre interrogación': '¿',
            'abre interrogacion': '¿',
            'cierra interrogación': '?',
            'cierra interrogacion': '?',
            'abre exclamación': '¡',
            'abre exclamacion': '¡',
            'cierra exclamación': '!',
            'cierra exclamacion': '!',
            'paréntesis abierto': '(',
            'parentesis abierto': '(',
            'paréntesis cerrado': ')',
            'parentesis cerrado': ')',
            'entre paréntesis': '(',
            'entre parentesis': '(',
            'comillas': '"',
            'abre comillas': '"',
            'cierra comillas': '"',
            'comilla simple': "'",
            'salto de línea': '\\n',
            'salto de linea': '\\n',
            'nueva línea': '\\n',
            'nueva linea': '\\n',
            'punto y aparte': '\\n',
            'aparte': '\\n',
            'guion': '-',
            'guión': '-',
            'asterisco': '*',
            'barra': '/',
            'barra invertida': '\\\\',
            'signo de igual': '=',
            'igual': '=',
            'más': '+',
            'mas': '+',
            'menos': '-',
            'por': '×',
            'dividido': '÷',
            'por ciento': '%',
            'porcentaje': '%',
            'símbolo de grado': '°',
            'grados': '°',
            'euro': '€',
            'dólar': '$',
            'dolar': '$',
            'libra': '£',
            'yen': '¥',
            'ampersand': '&',
            'y comercial': '&',
            'numeral': '#',
            'almohadilla': '#',
            'arroba': '@',
            'punto suspensivos': '...',
            'puntos suspensivos': '...',
            'suspensivos': '...'
        };

        // Inicializar reconocimiento de voz
        function initSpeechRecognition() {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            
            if (!SpeechRecognition) {
                showToast('❌ Tu navegador no soporta reconocimiento de voz. Usa Chrome, Edge o Safari.', 5000);
                return false;
            }

            recognition = new SpeechRecognition();
            recognition.continuous = true;
            recognition.interimResults = true;
            recognition.lang = 'es-ES';
            recognition.maxAlternatives = 1;

            recognition.onstart = function() {
                isRecording = true;
                isPaused = false;
                updateUI();
                showToast('🎙️ Grabación iniciada');
            };

            recognition.onresult = function(event) {
                interimTranscript = '';
                
                for (let i = event.resultIndex; i < event.results.length; i++) {
                    const transcript = event.results[i][0].transcript;
                    
                    if (event.results[i].isFinal) {
                        const processedText = processTranscript(transcript);
                        finalTranscript += processedText + ' ';
                    } else {
                        interimTranscript += transcript;
                    }
                }
                
                updateTextOutput();
                updateStats();
            };

            recognition.onerror = function(event) {
                console.error('Error de reconocimiento:', event.error);
                if (event.error === 'no-speech') {
                    // No hay habla, continuar grabando
                    return;
                }
                if (event.error === 'audio-capture') {
                    showToast('❌ No se detecta micrófono');
                } else if (event.error === 'not-allowed') {
                    showToast('❌ Permiso de micrófono denegado');
                    document.getElementById('permissionOverlay').classList.remove('hidden');
                } else {
                    showToast('⚠️ Error: ' + event.error);
                }
            };

            recognition.onend = function() {
                if (isRecording && !isPaused) {
                    // Reiniciar automáticamente si sigue grabando (evita cortes)
                    try {
                        recognition.start();
                    } catch(e) {
                        isRecording = false;
                        updateUI();
                    }
                } else {
                    updateUI();
                }
            };

            return true;
        }

        // Procesar transcripción y reemplazar comandos
        function processTranscript(text) {
            let processed = text.toLowerCase().trim();
            
            // Procesar comandos de puntuación
            Object.keys(punctuationMap).forEach(command => {
                const regex = new RegExp(`\\\\b${command}\\\\b`, 'gi');
                processed = processed.replace(regex, punctuationMap[command]);
            });

            // Procesar números escritos (opcional, mejora)
            processed = processed.replace(/\\bcero\\b/gi, '0')
                                .replace(/\\buno\\b/gi, '1')
                                .replace(/\\bdos\\b/gi, '2')
                                .replace(/\\btres\\b/gi, '3')
                                .replace(/\\bcuatro\\b/gi, '4')
                                .replace(/\\bcinco\\b/gi, '5')
                                .replace(/\\bseis\\b/gi, '6')
                                .replace(/\\bsiete\\b/gi, '7')
                                .replace(/\\bocho\\b/gi, '8')
                                .replace(/\\bnueve\\b/gi, '9');

            // Capitalizar primera letra después de punto
            processed = processed.replace(/([.!?])\\s+([a-záéíóúñ])/gi, (match, p1, p2) => {
                return p1 + ' ' + p2.toUpperCase();
            });

            // Capitalizar primera letra del texto
            if (finalTranscript.length === 0 || finalTranscript.endsWith('. ') || finalTranscript.endsWith('? ') || finalTranscript.endsWith('! ')) {
                processed = processed.charAt(0).toUpperCase() + processed.slice(1);
            }

            return processed;
        }

        // Actualizar salida de texto
        function updateTextOutput() {
            const textOutput = document.getElementById('textOutput');
            const displayText = finalTranscript + 
                (interimTranscript ? '<span class="interim-text">' + interimTranscript + '</span>' : '');
            
            // Para textarea, usamos value en lugar de innerHTML
            textOutput.value = finalTranscript + (interimTranscript ? ' [' + interimTranscript + ']' : '');
            
            // Auto-scroll al final
            textOutput.scrollTop = textOutput.scrollHeight;
        }

        // Actualizar estadísticas
        function updateStats() {
            const text = finalTranscript.trim();
            const words = text ? text.split(/\\s+/).length : 0;
            const chars = text.length;
            
            document.getElementById('wordCount').textContent = words;
            document.getElementById('charCount').textContent = chars;
        }

        // Actualizar temporizador
        function updateTimer() {
            if (!recordingStartTime) return;
            
            const elapsed = Math.floor((Date.now() - recordingStartTime) / 1000);
            const minutes = Math.floor(elapsed / 60).toString().padStart(2, '0');
            const seconds = (elapsed % 60).toString().padStart(2, '0');
            document.getElementById('timeCount').textContent = `${minutes}:${seconds}`;
        }

        // Actualizar UI
        function updateUI() {
            const btnToggle = document.getElementById('btnToggle');
            const btnStop = document.getElementById('btnStop');
            const statusIndicator = document.getElementById('statusIndicator');
            const statusText = document.getElementById('statusText');
            const textOutput = document.getElementById('textOutput');

            if (isRecording && !isPaused) {
                btnToggle.innerHTML = '⏸️ Pausar';
                btnToggle.classList.remove('btn-primary');
                btnToggle.classList.add('btn-warning');
                btnStop.disabled = false;
                statusIndicator.classList.add('recording');
                statusText.textContent = '🔴 Grabando...';
                textOutput.classList.add('recording-active');
            } else if (isPaused) {
                btnToggle.innerHTML = '▶️ Reanudar';
                btnToggle.classList.remove('btn-warning');
                btnToggle.classList.add('btn-primary');
                btnStop.disabled = false;
                statusIndicator.classList.remove('recording');
                statusIndicator.classList.add('active');
                statusText.textContent = '⏸️ Pausado';
                textOutput.classList.remove('recording-active');
            } else {
                btnToggle.innerHTML = '▶️ Iniciar Grabación';
                btnToggle.classList.remove('btn-warning');
                btnToggle.classList.add('btn-primary');
                btnStop.disabled = true;
                statusIndicator.classList.remove('recording', 'active');
                statusText.textContent = 'Listo para grabar';
                textOutput.classList.remove('recording-active');
            }
        }

        // Solicitar permiso de micrófono
        async function requestMicrophonePermission() {
            try {
                microphoneStream = await navigator.mediaDevices.getUserMedia({ audio: true });
                
                // Cerrar el stream temporal, solo necesitábamos el permiso
                microphoneStream.getTracks().forEach(track => track.stop());
                
                document.getElementById('permissionOverlay').classList.add('hidden');
                
                if (initSpeechRecognition()) {
                    showToast('✅ Micrófono habilitado correctamente');
                }
            } catch (err) {
                console.error('Error al obtener permiso:', err);
                showToast('❌ No se pudo acceder al micrófono. Por favor, verifica los permisos.');
            }
        }

        // Iniciar/Pausar grabación
        function toggleRecording() {
            if (!recognition) {
                if (!initSpeechRecognition()) return;
            }

            if (!isRecording) {
                // Iniciar
                try {
                    finalTranscript = document.getElementById('textOutput').value;
                    recognition.start();
                    recordingStartTime = Date.now();
                    timerInterval = setInterval(updateTimer, 1000);
                } catch(e) {
                    showToast('❌ Error al iniciar: ' + e.message);
                }
            } else if (!isPaused) {
                // Pausar
                isPaused = true;
                recognition.stop();
                clearInterval(timerInterval);
                updateUI();
                showToast('⏸️ Grabación pausada');
            } else {
                // Reanudar
                isPaused = false;
                try {
                    recognition.start();
                    timerInterval = setInterval(updateTimer, 1000);
                } catch(e) {
                    showToast('❌ Error al reanudar: ' + e.message);
                }
            }
        }

        // Detener grabación
        function stopRecording() {
            if (recognition) {
                isRecording = false;
                isPaused = false;
                recognition.stop();
                clearInterval(timerInterval);
                
                // Limpiar transcripción intermedia
                if (interimTranscript) {
                    const processed = processTranscript(interimTranscript);
                    finalTranscript += processed + ' ';
                    interimTranscript = '';
                    updateTextOutput();
                    updateStats();
                }
                
                updateUI();
                showToast('⏹️ Grabación detenida');
            }
        }

        // Copiar texto
        function copyText() {
            const textOutput = document.getElementById('textOutput');
            textOutput.select();
            document.execCommand('copy');
            
            // Deseleccionar
            window.getSelection().removeAllRanges();
            
            showToast('📋 Texto copiado al portapapeles');
        }

        // Limpiar texto
        function clearText() {
            if (confirm('¿Estás seguro de que quieres borrar todo el texto?')) {
                finalTranscript = '';
                interimTranscript = '';
                document.getElementById('textOutput').value = '';
                document.getElementById('wordCount').textContent = '0';
                document.getElementById('charCount').textContent = '0';
                document.getElementById('timeCount').textContent = '00:00';
                recordingStartTime = null;
                showToast('🗑️ Texto eliminado');
            }
        }

        // Mostrar notificación toast
        function showToast(message, duration = 3000) {
            const toast = document.getElementById('toast');
            toast.textContent = message;
            toast.classList.add('show');
            
            setTimeout(() => {
                toast.classList.remove('show');
            }, duration);
        }

        // Verificar permisos al cargar
        window.addEventListener('load', async () => {
            try {
                const devices = await navigator.mediaDevices.enumerateDevices();
                const hasMicrophone = devices.some(device => device.kind === 'audioinput');
                
                if (!hasMicrophone) {
                    showToast('❌ No se detecta ningún micrófono');
                }
            } catch(e) {
                console.error('Error al enumerar dispositivos:', e);
            }
        });

        // Atajo de teclado: Ctrl+Enter para iniciar/detener
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'Enter') {
                e.preventDefault();
                toggleRecording();
            }
            if (e.ctrlKey && e.key === 'c' && document.activeElement.id !== 'textOutput') {
                e.preventDefault();
                copyText();
            }
        });

        // Auto-guardar en localStorage
        document.getElementById('textOutput').addEventListener('input', () => {
            localStorage.setItem('speechText', document.getElementById('textOutput').value);
        });

        // Cargar texto guardado
        window.addEventListener('load', () => {
            const saved = localStorage.getItem('speechText');
            if (saved) {
                finalTranscript = saved;
                document.getElementById('textOutput').value = saved;
                updateStats();
            }
        });
    </script>
</body>
</html>'''

# Guardar el archivo
with open('/mnt/kimi/output/speech_to_text_app.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("✅ Aplicación Speech-to-Text creada exitosamente")
print("📁 Archivo guardado en: /mnt/kimi/output/speech_to_text_app.html")
