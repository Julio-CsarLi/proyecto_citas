Plataforma de Reserva de Citas Médicas

Este proyecto es una arquitectura de microservicios diseñada en Python para la gestión de reservas de citas médicas.

Tecnologías Utilizadas

* Lenguaje: Python (FastAPI / Flask)
* Contenedor: Docker & Docker Desktop
* Orquestación: Kubernetes (K8s)
* Service Mesh: Istio (mTLS & Observabilidad)
* Ingeniería del Caos: Chaos Mesh (Pruebas de resiliencia)
* CI/CD:** GitHub Actions

Prerrequisitos

asegúrate de tener instalado:
1. Docker Desktop (https://www.docker.com/products/docker-desktop/) con **Kubernetes habilitado**.
2. Git instalado en el sistema.
3. Helm v3 (para la gestión de paquetes de Chaos Mesh).


Guía de Despliegue Paso a Paso

1. Desplegar los Microservicios en Kubernetes
Aplica los manifiestos de Kubernetes para levantar los servicios de pacientes y agenda:
`kubectl apply -f k8s/pacientes.yaml`
`kubectl apply -f k8s/agenda.yaml`

2. Acceso a la Aplicación
La API Gateway expone el servicio de la agenda. Se interactuar con la documentación en:
**Swagger UI:** `http://localhost:8002/docs`

Seguridad y Observabilidad (Istio & Kiali)

El clúster utiliza Istio para cifrar de extremo a extremo las comunicaciones internas mediante Mutual TLS (mTLS) de forma transparente.

Para abrir el mapa de topología de red y telemetría en tiempo real:
1. Ejecuta el dashboard de Kiali: `.\istio-1.29.2\bin\istioctl.exe dashboard kiali`
2. En la pestaña Graph, selecciona el namespace `default y activa la opción **Security** en el menú *Display* para visualizar los candados de mTLS activos.

Ingeniería del Caos (Chaos Mesh)

Para comprobar la tolerancia a fallos del sistema, se realizan simulaciones de fallos controlados.

1.Iniciar el panel:** Ejecuta `kubectl port-forward -n chaos-testing svc/chaos-dashboard 2333:2333`
2.Acceder: Entra a `http://localhost:2333` e inicia sesión.
3.Simular: Configura un experimento de tipo Pod Fault (Pod Kill) apuntando a la etiqueta de la agenda.
4.Observar: Monitorea cómo Kubernetes destruye el pod afectado y levanta uno nuevo instantáneamente ejecutando `kubectl get pods -w`.

Pipeline de Integración Continua (CI)

El proyecto cuenta con un flujo automatizado en GitHub Actions configurado en la carpeta `.github/workflows`. 

Cada vez que se realiza una actualización en el código:
1. Un agente remoto clona el repositorio.
2. Construye y valida las imágenes de Docker.
3. Valida la integridad del código para asegurar que esté listo para producción.

Guía de Demostración del Proyecto


Paso 1: Demostrar la Orquesta y el Funcionamiento Base
Objetivo: Probar que los contenedores están vivos y se comunican entre sí.
Acción: Ejecuta `kubectl get pods` para mostrar que los contenedores están activos y con el proxy de Istio inyectado.
Acción: Abre `http://localhost:8002/docs` y envía una petición POST para demostrar que el sistema procesa datos correctamente.

Paso 2: El Mapa Visual y la Seguridad Zero-Trust
Objetivo: Demostrar la encriptación mTLS automática mediante Istio.
Acción: Abre el panel de Kiali y configura la vista para mostrar la seguridad.
Explicación: Los candados verdes en las conexiones del radar visual. Esto demuestra que la arquitectura es Zero-Trust y la comunicación viaja encriptada.

Paso 3: El Ataque del Caos (Resiliencia en Vivo)
Objetivo: Comprobar la auto-recuperación (Self-healing) del sistema.
Acción: Abre el panel de Chaos Mesh y ejecuta un ataque de muerte súbita contra la Agenda.
Explicación: En tiempo real cómo el sistema detecta la caída y levanta un clon exacto de la aplicación en milisegundos sin que nadie tenga que intervenir manualmente.

Paso 4: Automatización y Despliegue (CI/CD)
Objetivo: Mostrar que el desarrollo está automatizado y listo para la nube.
Acción: Mostrar la pestaña "Actions" en el repositorio de GitHub.
Explicación: Las palomitas verdes de éxito, demostrando que un robot en la nube revisa y construye la aplicación automáticamente cada vez que hay nuevo código.
