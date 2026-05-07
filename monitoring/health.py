from flask import jsonify


def health_check():
    return jsonify({
        "status": "ok",
        "service": "ai_job_agent",
        "version": "1.0.0"
    })