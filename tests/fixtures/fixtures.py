import pytest
import json

@pytest.fixture(scope='session')
def jobpost_simple():
    return {
        'title': 'Enfermera - Especialista Equipos Médicos/Pabellón',
        'source_url': 'https://www.chiletrabajos.cl/encuentra-un-empleo?2=enfermera&13=&fecha=3&categoria=&8=&14=&inclusion=&f=2',
        'posting_url': 'https://www.chiletrabajos.cl/trabajo/enfermera-especialista-equipos-medicos-pabellon-3374187',
        'company': 'Perceptual consultores ltda.',
        'geolocalization': 'Santiago',
        'work_schedule': 'Full-time',
        'employment_type': 'Plazo fijo y luego indefinido',

        'description': '''
        Empresa dedicada a la comercialización de productos tangibles del área de la Salud, solicita para incorporar a su Staff, Enfermera Universitaria para el Área I+D, Inglés Avanzado con al menos 5 años de experiencia en el área y o cargos similares.

        Objetivo del cargo: Colaborar en la investigación y desarrollo de nuevos productos o nuevas representaciones de dispositivos médicos y equipamiento.

        Responsabilidades:

        -Buscar productos de innovadores, nuevas técnicas médicas y usos de nuevos productos o procedimientos en los pacientes con el objetivo de mantener a la compañía actualizada de las nuevas tendencias que existen en el mundo.
        -Efectuar análisis de mercado y de nuevas técnicas y tendencias de la industria.
        -Efectuar propuesta de incorporación de productos con enfoque técnico económico y estudio de la competencia.
        -Coordinar con Consultores Clínicos el desarrollo de nuevos productos para el mercado nacional en base a la información de campo aportada por ellas.
        -Sugerir en forma proactiva productos que generen un valor agregado.
        -Velar por la planificación, seguimiento y control de las acciones realizadas en los proyectos.
        -Efectuar evaluación interna de los productos a través de herramientas estandarizadas de su responsabilidad.
        -Efectuar coordinación con Gerencia de Ventas para la evaluación de productos en clientes a través del equipo comercial previo a aprobación de Gerente General.
        -Efectuar la capacitación de la fuerza de ventas acerca de los productos a incorporar en el catálogo de la empresa.
        -Efectuar y mantener registro actualizado de cada etapa del proceso de Investigación y Desarrollo.
        -Asistencia a congresos y ferias de interés para el área de investigación y desarrollo.


        Condiciones Laborales.

        -Tipo de contrato inicial plazo fijo, luego indefinido
        -Horario lunes a viernes 8:00 a 17:30 hrs.
        -Modalidad: Presencial
        -Disponibilidad para viajar fuera de Chile

        Requisitos mínimos:

        De Educación:
        -Título profesional: Enfermera de casa de estudios reconocida por el Estado.
        -Diploma / Postgrado:
        -Infecciones relacionadas a la atención de Salud Obligatorio.
        -Deseable otro diplomado que complemente su función.
        -Obligatorio: Inglés escrito y hablado nivel alto.
        -Manejo de herramientas computacionales: Nivel alto.

        Experiencia:
        -Número de años: mínimo 5 años en cargo similar.
        -Experiencia clínica: mínimo 3 años en una unidad de Paciente Crítico.
        -Haber trabajo en Hospitales o clínicas, en área de Pabellón o UCI (manejo avanzado en insumos médicos).''',
    }

@pytest.fixture(scope='session')
def specialties():
    return {
        "Enfermería":["enfermer.?","\beu\b"],
        "Kinesiología":["kinesi.log.?","kinesiolog.?","fisioterapia","mesoterapia","erg.nomo","ergono[ií]a"],
        "TENS":{
            "Level1": ["r'tens?\b'"],
            "Level2": {
                "Patterns": ["t[eé]cnic","t[eé]c.?","tec"],
                "Patterns_lvl2": ["enfermer.?"]
            }
        },
        "Psicología":["psic.log.?","sicolog.","reclutador.?","reclutamiento","terapeuta","orientador laboral"]
    }
