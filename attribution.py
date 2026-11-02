import             'EXCHANGE': {'color': '#10b981', 'border': '#059669', 'size': 28, 'shape': 'box', 'icon': 'building'},
            'PGP': {'color': '#8b5cf6', 'border': '#7c3aed', 'size': 22, 'shape': 'triangle', 'icon': 'key'},
            'INFRASTRUCTURE': {'color': '#06b6d4', 'border': '#0891b2', 'size': 24, 'shape': 'square', 'icon': 'server'},
            'FORUM_ACCOUNT': {'color': '#6366f1', 'border': '#4f46e5', 'size': 22, 'shape': 'dot', 'icon': 'message'},
            'CLEARWEB': {'color': '#3b82f6', 'border': '#2563eb', 'size': 26, 'shape': 'box', 'icon': 'globe'},
            'IDENTITY': {'color': '#ec4899', 'border': '#db2777', 'size': 34, 'shape': 'star', 'icon': 'user-check'}
        }
        formatted_nodes = []
        for n in nodes:
            style = type_palette.get(n['type'], {'color': '#94a3b8', 'border': '#64748b', 'size': 20, 'shape': 'circle', 'icon': 'info'})
            formatted_nodes.append({
                'id': n['id'],
                'label': n['label'],
                'type': n['type'],
                'category': n['category'],
                'details': n.get('details', ''),
                'risk_weight': n.get('risk_weight', 50),
                'color': style['color'],
                'borderColor': style['border'],
                'size': style['size'],
                'icon': style['icon']
            })
        formatted_edges = []
        for e in edges:
            formatted_edges.append({
                'id': e.get('id'),
                'from': e['source_node'],
                'to': e['target_node'],
                'relation': e['relation'],
                'weight': e['evidence_weight'],
                'description': e['description'],
                'color': '#38bdf8' if e['evidence_weight'] >= 85 else '#94a3b8'
            })
        return {
            'nodes': formatted_nodes,
            'edges': formatted_edges,
            'total_nodes': len(formatted_nodes),
            'total_edges': len(formatted_edges)
        }