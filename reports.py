#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_report(attachment, title, summary):
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(summary, styles["BodyText"])
    table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_info])
