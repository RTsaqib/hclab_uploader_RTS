from sqlalchemy.exc import SQLAlchemyError

def select(engine:object, site:str)->list:
  '''
  Returns list of order from HIS table

  Parameters:
    engine : object
        Connection to HIS database
    
    site : str
        Site code
  '''
  
  sql = """
    select
    98 as id,
    message_dt,
    ono,
    order_control,
    pid,
    apid,
    name as pname,
    address1, address2, address3, address4,
    ptype,
    birth_dt,
    sex,
    '' as lno,
    request_dt,
    concat(source_cd, '^', source_nm) AS source,
    concat(clinician_cd, '^', clinician_nm) AS clinician,
    room_no,
    priority,
    '' as pstatus,
    comment,
    visitno,
    order_testid,
    address4 as email
    from lis_order WHERE ono="LAB0008" and flag= 0
  """
  #param = (site)
  try:
    with engine.connect() as conn:
        records = conn.execute(sql).fetchall()

  except SQLAlchemyError as e:
    raise Exception(f'HIS Database not found. {e}')

  return records