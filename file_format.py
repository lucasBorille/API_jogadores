def file_format(format = None, data = None):
    if format == 'csv':
        return data.to_csv(index=False)
    elif format == 'json':
        return data.to_json(orient='records')
    elif format == 'html':
        return data.to_html(index=False)
    elif format == 'txt':
        return data.to_csv(sep='\t', index=False)
    elif not format:
        return data.to_json(orient='records')
    else:
        return ('Invalid format', 400) 